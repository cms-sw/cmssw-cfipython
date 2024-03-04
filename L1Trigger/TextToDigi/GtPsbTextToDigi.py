import FWCore.ParameterSet.Config as cms

def GtPsbTextToDigi(**kwargs):
  mod = cms.EDProducer('GtPsbTextToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
