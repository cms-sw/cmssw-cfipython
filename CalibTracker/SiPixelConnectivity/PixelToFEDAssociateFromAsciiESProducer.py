import FWCore.ParameterSet.Config as cms

def PixelToFEDAssociateFromAsciiESProducer(**kwargs):
  mod = cms.ESProducer('PixelToFEDAssociateFromAsciiESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
