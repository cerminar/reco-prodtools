import FWCore.ParameterSet.Config as cms

from driver import process

process.maxEvents.input = cms.untracked.int32(DUMMYEVTSPERJOB)
process.RandomNumberGeneratorService.generator.initialSeed = cms.untracked.uint32(DUMMYSEED)
process.RandomNumberGeneratorService.VtxSmeared.initialSeed = cms.untracked.uint32(DUMMYSEED)
process.source.firstLuminosityBlock = cms.untracked.uint32(DUMMYSEED)
process.FEVTDEBUGHLToutput.fileName = cms.untracked.string('file:DUMMYFILENAME')

if hasattr(process.mix, 'input'):
    process.mix.input.fileNames = cms.untracked.vstring(PUFILELIST)


# FIXME: not sure how to handle this, for now we lesve it unchanged, not sure it works!
#DUMMYINCONESECTION
