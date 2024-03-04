import FWCore.ParameterSet.Config as cms

def PhoVIDNestedWPBitmapProducer(**kwargs):
  mod = cms.EDProducer('PhoVIDNestedWPBitmapProducer',
    src = cms.required.InputTag,
    srcForID = cms.InputTag(''),
    WorkingPoints = cms.required.vstring,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
