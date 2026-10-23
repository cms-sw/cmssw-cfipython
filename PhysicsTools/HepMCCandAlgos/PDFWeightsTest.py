import FWCore.ParameterSet.Config as cms

def PDFWeightsTest(*args, **kwargs):
  mod = cms.EDAnalyzer('PDFWeightsTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
