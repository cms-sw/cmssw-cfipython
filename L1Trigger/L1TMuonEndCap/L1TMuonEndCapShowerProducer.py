import FWCore.ParameterSet.Config as cms

def L1TMuonEndCapShowerProducer(**kwargs):
  mod = cms.EDProducer('L1TMuonEndCapShowerProducer',
    enableOneLooseShower = cms.bool(True),
    enableOneNominalShower = cms.bool(True),
    enableOneTightShower = cms.bool(True),
    enableTwoLooseShowers = cms.bool(False),
    CSCShowerInput = cms.InputTag('simCscTriggerPrimitiveDigis'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
