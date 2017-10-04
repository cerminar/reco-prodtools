import FWCore.ParameterSet.Config as cms

generator = cms.EDProducer("GUNPRODUCERTYPE",
    AddAntiParticle = cms.bool(True),
    PGunParameters = cms.PSet(
        MaxEta = cms.double(DUMMYETAMAX),
        MaxPhi = cms.double(3.14159265359),
        MAXTHRESHSTRING = cms.double(DUMMYTHRESHMAX),
        MinEta = cms.double(DUMMYETAMIN),
        MinPhi = cms.double(-3.14159265359),
        MINTHRESHSTRING = cms.double(DUMMYTHRESHMIN),
        #DUMMYINCONESECTION
        PartID = cms.vint32(DUMMYIDs)
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('multiple particles predefined pT/E eta 1p479 to 3')
)
