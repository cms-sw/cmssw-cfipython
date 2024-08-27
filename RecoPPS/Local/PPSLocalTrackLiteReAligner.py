import FWCore.ParameterSet.Config as cms

def PPSLocalTrackLiteReAligner(**kwargs):
  mod = cms.EDProducer('PPSLocalTrackLiteReAligner',
    inputTrackTag = cms.InputTag('ctppsLocalTrackLiteProducer'),
    alignmentTag = cms.ESInputTag('', ''),
    outputTrackTag = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
