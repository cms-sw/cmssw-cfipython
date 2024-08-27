import FWCore.ParameterSet.Config as cms

def PDFWeightsTest(**kwargs):
  mod = cms.EDAnalyzer('PDFWeightsTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
