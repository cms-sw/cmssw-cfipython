import FWCore.ParameterSet.Config as cms

def GenJetGenPartMerger(**kwargs):
  mod = cms.EDProducer('GenJetGenPartMerger',
    srcJet = cms.required.InputTag,
    srcPart = cms.required.InputTag,
    cut = cms.required.string,
    hasTauAnc = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
