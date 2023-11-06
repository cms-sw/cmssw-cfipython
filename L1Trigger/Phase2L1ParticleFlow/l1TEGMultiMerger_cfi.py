import FWCore.ParameterSet.Config as cms

l1TEGMultiMerger = cms.EDProducer('L1TEGMultiMerger',
  tkElectrons = cms.required.VPSet,
  tkEms = cms.required.VPSet,
  tkEgs = cms.required.VPSet,
  mightGet = cms.optional.untracked.vstring
)
