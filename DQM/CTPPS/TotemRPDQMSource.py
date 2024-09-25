import FWCore.ParameterSet.Config as cms

def TotemRPDQMSource(*args, **kwargs):
  mod = cms.EDProducer('TotemRPDQMSource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
