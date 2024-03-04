import FWCore.ParameterSet.Config as cms

def PixelToLNKAssociateFromAsciiESProducer(**kwargs):
  mod = cms.ESProducer('PixelToLNKAssociateFromAsciiESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
