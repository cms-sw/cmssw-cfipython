import FWCore.ParameterSet.Config as cms

def StripByStripTestDriver(*args, **kwargs):
  mod = cms.EDProducer('StripByStripTestDriver',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
