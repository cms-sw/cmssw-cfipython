import FWCore.ParameterSet.Config as cms

def PFTowers(**kwargs):
  mod = cms.EDProducer('PFTowers',
    useHF = cms.bool(True),
    src = cms.InputTag('particleFlow'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
