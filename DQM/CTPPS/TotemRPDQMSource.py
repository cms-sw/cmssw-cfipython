import FWCore.ParameterSet.Config as cms

def TotemRPDQMSource(**kwargs):
  mod = cms.EDProducer('TotemRPDQMSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
