import FWCore.ParameterSet.Config as cms

def PixelToFEDAssociateFromAsciiESProducer(*args, **kwargs):
  mod = cms.ESProducer('PixelToFEDAssociateFromAsciiESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
