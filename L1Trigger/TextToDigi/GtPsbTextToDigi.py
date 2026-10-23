import FWCore.ParameterSet.Config as cms

def GtPsbTextToDigi(*args, **kwargs):
  mod = cms.EDProducer('GtPsbTextToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
