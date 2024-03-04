import FWCore.ParameterSet.Config as cms

def PPSAlignmentWorker(**kwargs):
  mod = cms.EDProducer('PPSAlignmentWorker',
    label = cms.string(''),
    tracksTags = cms.VInputTag('ctppsLocalTrackLiteProducer'),
    dqm_dir = cms.string('AlCaReco/PPSAlignment'),
    debug = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
