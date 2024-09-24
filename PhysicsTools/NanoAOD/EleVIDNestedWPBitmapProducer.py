import FWCore.ParameterSet.Config as cms

def EleVIDNestedWPBitmapProducer(*args, **kwargs):
  mod = cms.EDProducer('EleVIDNestedWPBitmapProducer',
    src = cms.required.InputTag,
    srcForID = cms.InputTag(''),
    WorkingPoints = cms.required.vstring,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
