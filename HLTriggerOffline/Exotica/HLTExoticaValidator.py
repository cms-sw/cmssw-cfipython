import FWCore.ParameterSet.Config as cms

def HLTExoticaValidator(*args, **kwargs):
  mod = cms.EDProducer('HLTExoticaValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
