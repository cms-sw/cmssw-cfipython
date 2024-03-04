import FWCore.ParameterSet.Config as cms

def L1TPFCandMultiMerger(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
