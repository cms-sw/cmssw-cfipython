import FWCore.ParameterSet.Config as cms

def EvFFEDSelector(**kwargs):
  mod = cms.EDProducer('EvFFEDSelector',
    inputTag = cms.InputTag('source'),
    fedList = cms.vuint32(
      812,
      1023
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
