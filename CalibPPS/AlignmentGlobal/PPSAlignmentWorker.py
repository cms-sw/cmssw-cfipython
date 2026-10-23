import FWCore.ParameterSet.Config as cms

def PPSAlignmentWorker(*args, **kwargs):
  mod = cms.EDProducer('PPSAlignmentWorker',
    label = cms.string(''),
    tracksTags = cms.VInputTag('ctppsLocalTrackLiteProducer'),
    dqm_dir = cms.string('AlCaReco/PPSAlignment'),
    debug = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
