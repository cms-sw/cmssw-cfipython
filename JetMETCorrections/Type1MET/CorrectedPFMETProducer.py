import FWCore.ParameterSet.Config as cms

def CorrectedPFMETProducer(**kwargs):
  mod = cms.EDProducer('CorrectedPFMETProducer',
    src = cms.InputTag('pfMet'),
    srcCorrections = cms.VInputTag('corrPfMetType1:type1'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
