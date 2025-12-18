import FWCore.ParameterSet.Config as cms

def QIE10Task(*args, **kwargs):
  mod = cms.EDProducer('QIE10Task',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
