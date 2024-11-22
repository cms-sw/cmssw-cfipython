import FWCore.ParameterSet.Config as cms

def EvFFEDSelector(*args, **kwargs):
  mod = cms.EDProducer('EvFFEDSelector',
    inputTag = cms.InputTag('source'),
    fedList = cms.vuint32(
      812,
      1023
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
