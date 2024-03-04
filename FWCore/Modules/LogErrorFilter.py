import FWCore.ParameterSet.Config as cms

def LogErrorFilter(**kwargs):
  mod = cms.EDFilter('LogErrorFilter',
    harvesterTag = cms.required.InputTag,
    atLeastOneError = cms.required.bool,
    atLeastOneWarning = cms.required.bool,
    useThresholdsPerKind = cms.required.bool,
    maxErrorKindsPerLumi = cms.uint32(999999),
    maxWarningKindsPerLumi = cms.uint32(999999),
    avoidCategories = cms.required.vstring,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
