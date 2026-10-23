import FWCore.ParameterSet.Config as cms

def MayConsumeWhatsIt(*args, **kwargs):
  mod = cms.ESProducer('MayConsumeWhatsIt',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
