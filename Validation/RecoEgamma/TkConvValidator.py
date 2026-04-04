import FWCore.ParameterSet.Config as cms

def TkConvValidator(*args, **kwargs):
  mod = cms.EDProducer('TkConvValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
