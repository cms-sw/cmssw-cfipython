import FWCore.ParameterSet.Config as cms

def MtdTruthDumper(**kwargs):
  mod = cms.EDAnalyzer('MtdTruthDumper',
    moduleLabelMtdSimLC = cms.InputTag('mix', 'MergedMtdTruthLC'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
