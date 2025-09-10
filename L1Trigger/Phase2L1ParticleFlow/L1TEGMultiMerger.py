import FWCore.ParameterSet.Config as cms

def L1TEGMultiMerger(*args, **kwargs):
  mod = cms.EDProducer('L1TEGMultiMerger',
    tkElectrons = cms.required.VPSet,
    tkEms = cms.required.VPSet,
    tkEgs = cms.required.VPSet,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
