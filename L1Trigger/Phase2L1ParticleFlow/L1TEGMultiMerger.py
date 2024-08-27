import FWCore.ParameterSet.Config as cms

def L1TEGMultiMerger(**kwargs):
  mod = cms.EDProducer('L1TEGMultiMerger',
    tkElectrons = cms.required.VPSet,
    tkEms = cms.required.VPSet,
    tkEgs = cms.required.VPSet,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
