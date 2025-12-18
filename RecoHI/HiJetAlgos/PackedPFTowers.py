import FWCore.ParameterSet.Config as cms

def PackedPFTowers(*args, **kwargs):
  mod = cms.EDProducer('PackedPFTowers',
    useHF = cms.bool(True),
    src = cms.InputTag('packedPFCandidates'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
