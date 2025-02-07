import FWCore.ParameterSet.Config as cms

def PFTowers(*args, **kwargs):
  mod = cms.EDProducer('PFTowers',
    useHF = cms.bool(True),
    src = cms.InputTag('particleFlow'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
