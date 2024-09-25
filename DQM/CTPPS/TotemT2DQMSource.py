import FWCore.ParameterSet.Config as cms

def TotemT2DQMSource(*args, **kwargs):
  mod = cms.EDProducer('TotemT2DQMSource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
