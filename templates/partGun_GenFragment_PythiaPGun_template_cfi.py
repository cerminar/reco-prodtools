import FWCore.ParameterSet.Config as cms

generator = cms.EDFilter("GUNPRODUCERTYPE",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    PGunParameters = cms.PSet(
      ParticleID = cms.vint32(DUMMYIDs),
      AddAntiParticle = cms.bool(True),
      MinPhi = cms.double(-3.14159265359),
      MaxPhi = cms.double(3.14159265359),
      MINTHRESHSTRING = cms.double(DUMMYTHRESHMIN),
      MAXTHRESHSTRING = cms.double(DUMMYTHRESHMAX),
      MinEta = cms.double(1.479),
      MaxEta = cms.double(3.0)
      ),
    PythiaParameters = cms.PSet(parameterSets = cms.vstring())
)
