import FWCore.ParameterSet.Config as cms

def HLTGenValClient(*args, **kwargs):
  mod = cms.EDProducer('HLTGenValClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
