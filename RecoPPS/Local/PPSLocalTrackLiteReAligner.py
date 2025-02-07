import FWCore.ParameterSet.Config as cms

def PPSLocalTrackLiteReAligner(*args, **kwargs):
  mod = cms.EDProducer('PPSLocalTrackLiteReAligner',
    inputTrackTag = cms.InputTag('ctppsLocalTrackLiteProducer'),
    alignmentTag = cms.ESInputTag('', ''),
    outputTrackTag = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
