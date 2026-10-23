import FWCore.ParameterSet.Config as cms

def PixelToLNKAssociateFromAsciiESProducer(*args, **kwargs):
  mod = cms.ESProducer('PixelToLNKAssociateFromAsciiESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
