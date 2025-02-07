import FWCore.ParameterSet.Config as cms

def MtdTruthDumper(*args, **kwargs):
  mod = cms.EDAnalyzer('MtdTruthDumper',
    moduleLabelMtdSimLC = cms.InputTag('mix', 'MergedMtdTruthLC'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
