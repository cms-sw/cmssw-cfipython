import FWCore.ParameterSet.Config as cms

def AlignmentProducerAsAnalyzer(**kwargs):
  mod = cms.EDProducer('AlignmentProducerAsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
