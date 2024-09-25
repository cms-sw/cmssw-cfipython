import FWCore.ParameterSet.Config as cms

def CorrectedPFMETProducer(*args, **kwargs):
  mod = cms.EDProducer('CorrectedPFMETProducer',
    src = cms.InputTag('pfMet'),
    srcCorrections = cms.VInputTag('corrPfMetType1:type1'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
