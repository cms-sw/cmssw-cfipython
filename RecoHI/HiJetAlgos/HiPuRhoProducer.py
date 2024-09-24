import FWCore.ParameterSet.Config as cms

def HiPuRhoProducer(**kwargs):
  mod = cms.EDProducer('HiPuRhoProducer',
    src = cms.InputTag('PFTowers'),
    medianWindowWidth = cms.int32(2),
    towSigmaCut = cms.double(5),
    puPtMin = cms.double(15),
    rParam = cms.double(0.3),
    nSigmaPU = cms.double(1),
    radiusPU = cms.double(0.5),
    minimumTowersFraction = cms.double(0.7),
    dropZeroTowers = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod