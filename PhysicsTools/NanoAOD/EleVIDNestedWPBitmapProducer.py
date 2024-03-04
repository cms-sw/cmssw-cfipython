import FWCore.ParameterSet.Config as cms

def EleVIDNestedWPBitmapProducer(**kwargs):
  mod = cms.EDProducer('EleVIDNestedWPBitmapProducer',
    src = cms.required.InputTag,
    srcForID = cms.InputTag(''),
    WorkingPoints = cms.required.vstring,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
