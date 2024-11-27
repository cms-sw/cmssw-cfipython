import FWCore.ParameterSet.Config as cms

def ShiftedPFJetProducer(*args, **kwargs):
  mod = cms.EDProducer('ShiftedPFJetProducer',
    src = cms.required.InputTag,
    jecUncertaintyValue = cms.optional.double,
    jetCorrUncertaintyTag = cms.optional.string,
    jetCorrInputFileName = cms.optional.FileInPath,
    jetCorrPayloadName = cms.optional.string,
    addResidualJES = cms.required.bool,
    jetCorrLabelUpToL3 = cms.optional.InputTag,
    jetCorrLabelUpToL3Res = cms.optional.InputTag,
    jetCorrEtaMax = cms.double(9.9),
    shiftBy = cms.required.double,
    verbosity = cms.untracked.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
