import FWCore.ParameterSet.Config as cms

def L1TMuonEndCapShowerProducer(*args, **kwargs):
  mod = cms.EDProducer('L1TMuonEndCapShowerProducer',
    enableOneLooseShower = cms.bool(True),
    enableOneNominalShower = cms.bool(True),
    enableOneTightShower = cms.bool(True),
    enableTwoLooseShowers = cms.bool(False),
    CSCShowerInput = cms.InputTag('simCscTriggerPrimitiveDigis'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
