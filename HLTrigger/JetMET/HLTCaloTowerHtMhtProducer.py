import FWCore.ParameterSet.Config as cms

def HLTCaloTowerHtMhtProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTCaloTowerHtMhtProducer',
    usePt = cms.bool(False),
    minPtTowerHt = cms.double(1),
    minPtTowerMht = cms.double(1),
    maxEtaTowerHt = cms.double(5),
    maxEtaTowerMht = cms.double(5),
    towersLabel = cms.InputTag('hltTowerMakerForAll'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
