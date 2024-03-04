import FWCore.ParameterSet.Config as cms

def HLTCaloTowerHtMhtProducer(**kwargs):
  mod = cms.EDProducer('HLTCaloTowerHtMhtProducer',
    usePt = cms.bool(False),
    minPtTowerHt = cms.double(1),
    minPtTowerMht = cms.double(1),
    maxEtaTowerHt = cms.double(5),
    maxEtaTowerMht = cms.double(5),
    towersLabel = cms.InputTag('hltTowerMakerForAll'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
