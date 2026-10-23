import FWCore.ParameterSet.Config as cms

def GenJetGenPartMerger(*args, **kwargs):
  mod = cms.EDProducer('GenJetGenPartMerger',
    srcJet = cms.required.InputTag,
    srcPart = cms.required.InputTag,
    cut = cms.required.string,
    hasTauAnc = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
