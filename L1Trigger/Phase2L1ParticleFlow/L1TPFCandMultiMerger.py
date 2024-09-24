import FWCore.ParameterSet.Config as cms

def L1TPFCandMultiMerger(*args, **kwargs):
  mod = cms.EDProducer('L1TPFCandMultiMerger',
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
