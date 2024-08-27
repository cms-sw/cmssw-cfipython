import FWCore.ParameterSet.Config as cms

def StripByStripTestDriver(**kwargs):
  mod = cms.EDProducer('StripByStripTestDriver',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
