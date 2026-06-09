import FWCore.ParameterSet.Config as cms

def PatFromScoutingPhotonProducer(*args, **kwargs):
  mod = cms.EDProducer('PatFromScoutingPhotonProducer',
    src = cms.InputTag('hltScoutingEgammaPacker'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
