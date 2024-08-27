import FWCore.ParameterSet.Config as cms

def PackedPFTowers(**kwargs):
  mod = cms.EDProducer('PackedPFTowers',
    useHF = cms.bool(True),
    src = cms.InputTag('packedPFCandidates'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
