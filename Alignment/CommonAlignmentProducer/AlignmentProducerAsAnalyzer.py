import FWCore.ParameterSet.Config as cms

def AlignmentProducerAsAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('AlignmentProducerAsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
