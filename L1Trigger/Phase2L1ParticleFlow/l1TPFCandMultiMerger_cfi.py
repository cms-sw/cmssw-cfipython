import FWCore.ParameterSet.Config as cms

l1TPFCandMultiMerger = cms.EDProducer('L1TPFCandMultiMerger',
  pfProducers = cms.VInputTag(
    'l1tLayer1Barrel',
    'l1tLayer1HGCal',
    'l1tLayer1HGCalNoTK',
    'l1tLayer1HF'
  ),
  labelsToMerge = cms.vstring(
    'PF',
    'Puppi',
    'Calo',
    'TK'
  ),
  regionalLabelsToMerge = cms.vstring('Puppi'),
  mightGet = cms.optional.untracked.vstring
)
